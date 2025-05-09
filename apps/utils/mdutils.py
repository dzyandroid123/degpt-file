from langchain_community.document_loaders import UnstructuredMarkdownLoader

class MdUtils:
        
    def text_data(self, file_path: str):
        try:
            loader = UnstructuredMarkdownLoader(file_path)
            data = loader.load()
            return data
        except Exception as e:
            print("============", e)
            return None
    
MdUtilsInstance = MdUtils()