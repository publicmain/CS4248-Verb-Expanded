# from transformers.utils.hub import hf_hub_download
# try:
#     # 这里尝试下载（或加载）config.json
#     config_file = hf_hub_download("facebook/bart-large-mnli", filename="config.json", local_files_only=False)
#     print("找到了文件：", config_file)
# except Exception as e:
#     print("在本地缓存中找不到文件：", e)
# # # Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-mnli")
# model = AutoModelForSequenceClassification.from_pretrained("facebook/bart-large-mnli")
proxies = {"http": "http://your-proxy-address:port", "https": "http://your-proxy-address:port"}
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-mnli", local_files_only=False, proxies=proxies)
