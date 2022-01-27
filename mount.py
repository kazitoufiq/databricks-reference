dbutils.fs.mount(
  source = "wasbs://iddddd.blob.core.windows.net",
  mount_point = "/mnt/xxxxxxx",
  extra_configs = {"fs.azure.account.key.xxxx.blob.core.windows.net":dbutils.secrets.get(scope = "yyyy", key = "dddd")})
