
class PreviewImage:
    CATEGORY = "example"
    
    @classmethod    
    def INPUT_TYPES(s):
        return { 
            "required": {
                "images": ("IMAGE",),  
                "index": ("INT", {      
                    "default": 0, 
                    "min": 0, 
                    "max": 100,  
                    "step": 1, 
                    "display": "number"
                })
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "preview_image"

    def preview_image(self, images, index):
        index = max(0, min(index, images.shape[0] - 1))
        
        result = images[index].unsqueeze(0)  
        return (result,)
