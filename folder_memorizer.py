import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
from pathlib import Path

class FolderMemorizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Path Memorizer")
        self.root.geometry("800x600")
        
        # Data file to store folder paths
        self.data_file = "folder_paths.json"
        self.folders = self.load_data()
        
        self.setup_ui()
        self.refresh_list()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Add folder section
        ttk.Label(main_frame, text="Add New Folder:", font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=(0, 10))
        
        ttk.Label(main_frame, text="Folder Name:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5))
        self.name_entry = ttk.Entry(main_frame, width=30)
        self.name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        ttk.Button(main_frame, text="Browse Folder", command=self.browse_folder).grid(row=1, column=2)
        
        ttk.Label(main_frame, text="Folder Path:").grid(row=2, column=0, sticky=tk.W, padx=(0, 5))
        self.path_entry = ttk.Entry(main_frame, width=50)
        self.path_entry.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 10))
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Button(buttons_frame, text="Add Folder", command=self.add_folder).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="Delete Selected", command=self.delete_folder).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="Open Folder", command=self.open_folder).pack(side=tk.LEFT, padx=(0, 10))
        
        # Search section
        search_frame = ttk.Frame(main_frame)
        search_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        search_frame.columnconfigure(1, weight=1)
        
        ttk.Label(search_frame, text="Search:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        self.search_entry.bind('<KeyRelease>', self.search_folders)
        
        ttk.Button(search_frame, text="Clear", command=self.clear_search).grid(row=0, column=2)
        
        # Folder list
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # Treeview for folder list
        columns = ('Name', 'Path')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        
        # Define column headings
        self.tree.heading('Name', text='Folder Name')
        self.tree.heading('Path', text='Folder Path')
        
        # Configure column widths
        self.tree.column('Name', width=200)
        self.tree.column('Path', width=500)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Grid treeview and scrollbar
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Double-click to open folder
        self.tree.bind('<Double-1>', self.on_double_click)
    
    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder_path)
            
            # Auto-fill name if empty
            if not self.name_entry.get():
                folder_name = os.path.basename(folder_path)
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, folder_name)
    
    def add_folder(self):
        name = self.name_entry.get().strip()
        path = self.path_entry.get().strip()
        
        if not name or not path:
            messagebox.showwarning("Input Error", "Please enter both folder name and path.")
            return
        
        if not os.path.exists(path):
            messagebox.showwarning("Path Error", "The specified path does not exist.")
            return
        
        if name in self.folders:
            messagebox.showwarning("Duplicate", "A folder with this name already exists.")
            return
        
        self.folders[name] = path
        self.save_data()
        self.refresh_list()
        
        # Clear entries
        self.name_entry.delete(0, tk.END)
        self.path_entry.delete(0, tk.END)
        
        messagebox.showinfo("Success", f"Folder '{name}' added successfully!")
    
    def delete_folder(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a folder to delete.")
            return
        
        item = self.tree.item(selected_item)
        folder_name = item['values'][0]
        
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{folder_name}'?"):
            del self.folders[folder_name]
            self.save_data()
            self.refresh_list()
            messagebox.showinfo("Success", f"Folder '{folder_name}' deleted successfully!")
    
    def open_folder(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a folder to open.")
            return
        
        item = self.tree.item(selected_item)
        folder_path = item['values'][1]
        
        try:
            if os.name == 'nt':  # Windows
                os.startfile(folder_path)
            elif os.name == 'posix':  # macOS and Linux
                os.system(f'open "{folder_path}"' if os.uname().sysname == 'Darwin' else f'xdg-open "{folder_path}"')
        except Exception as e:
            messagebox.showerror("Error", f"Could not open folder: {str(e)}")
    
    def on_double_click(self, event):
        self.open_folder()
    
    def search_folders(self, event=None):
        search_term = self.search_entry.get().lower()
        
        # Clear current items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add filtered items
        for name, path in self.folders.items():
            if search_term in name.lower() or search_term in path.lower():
                self.tree.insert('', tk.END, values=(name, path))
    
    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.refresh_list()
    
    def refresh_list(self):
        # Clear current items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add all folders
        for name, path in sorted(self.folders.items()):
            self.tree.insert('', tk.END, values=(name, path))
    
    def load_data(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load data: {str(e)}")
        return {}
    
    def save_data(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.folders, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save data: {str(e)}")

def main():
    root = tk.Tk()
    app = FolderMemorizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()