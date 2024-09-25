

class OCRInstaller:
    """
    OCR 安装器，负责根据 CPU 特性选择合适的 OCR 工具，并处理安装过程。
    """

    def __init__(self, logger: Optional[Logger] = None):
        self.logger = logger
        self.ocr_name, self.ocr_path = self._determine_ocr()

    def _cpu_support_avx2(self):
        """
        判断 CPU 是否支持 AVX2 指令集。
        """
        return cpufeature.CPUFeature["AVX2"]

    def _determine_ocr(self):
        """
        根据 CPU 是否支持 AVX2 指令集来决定使用的 OCR 工具。
        """
        if self._cpu_support_avx2():
            ocr_name = "PaddleOCR-json"
            ocr_path = r".\3rdparty\PaddleOCR-json_v.1.3.1\PaddleOCR-json.exe"
            self.logger.debug(f"CPU 支持 AVX2 指令集，使用 {ocr_name}")
        else:
            ocr_name = "RapidOCR-json"
            ocr_path = r".\3rdparty\RapidOCR-json_v0.2.0\RapidOCR-json.exe"
            self.logger.debug(f"CPU 不支持 AVX2 指令集，使用 {ocr_name}")
        return ocr_name, ocr_path

    def install_ocr(self):
        """
        安装选定的 OCR 工具。
        """
        from module.update.update_handler import UpdateHandler
        from tasks.base.fastest_mirror import FastestMirror

        base_url = "https://github.com/{name}/releases/download/{version}/{filename}"
        if self.ocr_name == "PaddleOCR-json":
            url = FastestMirror.get_github_mirror(base_url.format(name="hiroi-sora/PaddleOCR-json", version="v1.3.1", filename="PaddleOCR-json_v.1.3.1.7z"))
            version = "PaddleOCR-json_v.1.3.1"
        else:
            url = FastestMirror.get_github_mirror(base_url.format(name="hiroi-sora/RapidOCR-json", version="v0.2.0", filename="RapidOCR-json_v0.2.0.7z"))
            version = "RapidOCR-json_v0.2.0"

        update_handler = UpdateHandler(url, os.path.dirname(self.ocr_path), version)
        update_handler.run()

    def check_and_install(self):
        """
        检查 OCR 工具是否已安装，如未安装则进行安装。
        """
        if not os.path.exists(self.ocr_path):
            self.logger.warning(f"OCR 路径不存在: {self.ocr_path}")
            self.install_ocr()