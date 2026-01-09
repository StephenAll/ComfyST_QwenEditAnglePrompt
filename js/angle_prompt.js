import { app } from "../../scripts/app.js";

const NODE_CONFIGS = {
    "QwenAnglePromptEN": {
        defaultCamera: "Close-up",
        prompts: {
            "Close-up": [
                "front view low-angle shot close-up",
                "front-right quarter view low-angle shot close-up",
                "right side view low-angle shot close-up",
                "back-right quarter view low-angle shot close-up",
                "back view low-angle shot close-up",
                "back-left quarter view low-angle shot close-up",
                "left side view low-angle shot close-up",
                "front-left quarter view low-angle shot close-up",
                "front view eye-level shot close-up",
                "front-right quarter view eye-level shot close-up",
                "right side view eye-level shot close-up",
                "back-right quarter view eye-level shot close-up",
                "back view eye-level shot close-up",
                "back-left quarter view eye-level shot close-up",
                "left side view eye-level shot close-up",
                "front-left quarter view eye-level shot close-up",
                "front view elevated shot close-up",
                "front-right quarter view elevated shot close-up",
                "right side view elevated shot close-up",
                "back-right quarter view elevated shot close-up",
                "back view elevated shot close-up",
                "back-left quarter view elevated shot close-up",
                "left side view elevated shot close-up",
                "front-left quarter view elevated shot close-up",
                "front view high-angle shot close-up",
                "front-right quarter view high-angle shot close-up",
                "right side view high-angle shot close-up",
                "back-right quarter view high-angle shot close-up",
                "back view high-angle shot close-up",
                "back-left quarter view high-angle shot close-up",
                "left side view high-angle shot close-up",
                "front-left quarter view high-angle shot close-up",
            ],
            "Medium Shot": [
                "front view low-angle shot medium shot",
                "front-right quarter view low-angle shot medium shot",
                "right side view low-angle shot medium shot",
                "back-right quarter view low-angle shot medium shot",
                "back view low-angle shot medium shot",
                "back-left quarter view low-angle shot medium shot",
                "left side view low-angle shot medium shot",
                "front-left quarter view low-angle shot medium shot",
                "front view eye-level shot medium shot",
                "front-right quarter view eye-level shot medium shot",
                "right side view eye-level shot medium shot",
                "back-right quarter view eye-level shot medium shot",
                "back view eye-level shot medium shot",
                "back-left quarter view eye-level shot medium shot",
                "left side view eye-level shot medium shot",
                "front-left quarter view eye-level shot medium shot",
                "front view elevated shot medium shot",
                "front-right quarter view elevated shot medium shot",
                "right side view elevated shot medium shot",
                "back-right quarter view elevated shot medium shot",
                "back view elevated shot medium shot",
                "back-left quarter view elevated shot medium shot",
                "left side view elevated shot medium shot",
                "front-left quarter view elevated shot medium shot",
                "front view high-angle shot medium shot",
                "front-right quarter view high-angle shot medium shot",
                "right side view high-angle shot medium shot",
                "back-right quarter view high-angle shot medium shot",
                "back view high-angle shot medium shot",
                "back-left quarter view high-angle shot medium shot",
                "left side view high-angle shot medium shot",
                "front-left quarter view high-angle shot medium shot",
            ],
            "Wide Shot": [
                "front view low-angle shot wide shot",
                "front-right quarter view low-angle shot wide shot",
                "right side view low-angle shot wide shot",
                "back-right quarter view low-angle shot wide shot",
                "back view low-angle shot wide shot",
                "back-left quarter view low-angle shot wide shot",
                "left side view low-angle shot wide shot",
                "front-left quarter view low-angle shot wide shot",
                "front view eye-level shot wide shot",
                "front-right quarter view eye-level shot wide shot",
                "right side view eye-level shot wide shot",
                "back-right quarter view eye-level shot wide shot",
                "back view eye-level shot wide shot",
                "back-left quarter view eye-level shot wide shot",
                "left side view eye-level shot wide shot",
                "front-left quarter view eye-level shot wide shot",
                "front view elevated shot wide shot",
                "front-right quarter view elevated shot wide shot",
                "right side view elevated shot wide shot",
                "back-right quarter view elevated shot wide shot",
                "back view elevated shot wide shot",
                "back-left quarter view elevated shot wide shot",
                "left side view elevated shot wide shot",
                "front-left quarter view elevated shot wide shot",
                "front view high-angle shot wide shot",
                "front-right quarter view high-angle shot wide shot",
                "right side view high-angle shot wide shot",
                "back-right quarter view high-angle shot wide shot",
                "back view high-angle shot wide shot",
                "back-left quarter view high-angle shot wide shot",
                "left side view high-angle shot wide shot",
                "front-left quarter view high-angle shot wide shot",
            ],
        }
    },
    "QwenAnglePromptCN": {
        defaultCamera: "特写镜头组",
        prompts: {
            "特写镜头组": [
                "正面低仰角特写",
                "右前方低仰角特写",
                "右侧面低仰角特写",
                "右后方低仰角特写",
                "背面低仰角特写",
                "左后方低仰角特写",
                "左侧面低仰角特写",
                "左前方低仰角特写",
                "正面平视特写",
                "右前方平视特写",
                "右侧面平视特写",
                "右后方平视特写",
                "背面平视特写",
                "左后方平视特写",
                "左侧面平视特写",
                "左前方平视特写",
                "正面高位特写",
                "右前方高位特写",
                "右侧面高位特写",
                "右后方高位特写",
                "背面高位特写",
                "左后方高位特写",
                "左侧面高位特写",
                "左前方高位特写",
                "正面高角度俯拍特写",
                "右前方高角度俯拍特写",
                "右侧面高角度俯拍特写",
                "右后方高角度俯拍特写",
                "背面高角度俯拍特写",
                "左后方高角度俯拍特写",
                "左侧面高角度俯拍特写",
                "左前方高角度俯拍特写",
            ],
            "中景镜头组": [
                "正面低仰角中景",
                "右前方低仰角中景",
                "右侧面低仰角中景",
                "右后方低仰角中景",
                "背面低仰角中景",
                "左后方低仰角中景",
                "左侧面低仰角中景",
                "左前方低仰角中景",
                "正面平视中景",
                "右前方平视中景",
                "右侧面平视中景",
                "右后方平视中景",
                "背面平视中景",
                "左后方平视中景",
                "左侧面平视中景",
                "左前方平视中景",
                "正面高位中景",
                "右前方高位中景",
                "右侧面高位中景",
                "右后方高位中景",
                "背面高位中景",
                "左后方高位中景",
                "左侧面高位中景",
                "左前方高位中景",
                "正面高角度俯拍中景",
                "右前方高角度俯拍中景",
                "右侧面高角度俯拍中景",
                "右后方高角度俯拍中景",
                "背面高角度俯拍中景",
                "左后方高角度俯拍中景",
                "左侧面高角度俯拍中景",
                "左前方高角度俯拍中景",
            ],
            "全景镜头组": [
                "正面低仰角全景",
                "右前方低仰角全景",
                "右侧面低仰角全景",
                "右后方低仰角全景",
                "背面低仰角全景",
                "左后方低仰角全景",
                "左侧面低仰角全景",
                "左前方低仰角全景",
                "正面平视全景",
                "右前方平视全景",
                "右侧面平视全景",
                "右后方平视全景",
                "背面平视全景",
                "左后方平视全景",
                "左侧面平视全景",
                "左前方平视全景",
                "正面高位全景",
                "右前方高位全景",
                "右侧面高位全景",
                "右后方高位全景",
                "背面高位全景",
                "左后方高位全景",
                "左侧面高位全景",
                "左前方高位全景",
                "正面高角度俯拍全景",
                "右前方高角度俯拍全景",
                "右侧面高角度俯拍全景",
                "右后方高角度俯拍全景",
                "背面高角度俯拍全景",
                "左后方高角度俯拍全景",
                "左侧面高角度俯拍全景",
                "左前方高角度俯拍全景",
            ],
        }
    }
};

function registerAnglePromptNode(nodeName) {
    const config = NODE_CONFIGS[nodeName];
    if (!config) return;

    app.registerExtension({
        name: nodeName,
        async beforeRegisterNodeDef(nodeType, nodeData) {
            if (nodeData.name !== nodeName) return;

            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                onNodeCreated?.apply(this, arguments);

                const cameraWidget = this.widgets.find(w => w.name === "camera");
                const splicingWidget = this.widgets.find(w => w.name === "splicing");
                const defaultPrompts = config.prompts[config.defaultCamera];
                
                // Find the index of splicing widget to insert prompt before it
                const splicingIndex = this.widgets.indexOf(splicingWidget);
                
                const promptWidget = this.addWidget(
                    "combo",
                    "prompt",
                    defaultPrompts[0],
                    () => {},
                    { values: defaultPrompts }
                );

                // Move prompt widget to be after camera and before splicing
                if (splicingIndex > 0) {
                    this.widgets.pop(); // Remove the just added prompt widget from end
                    this.widgets.splice(splicingIndex, 0, promptWidget); // Insert before splicing
                }

                const updatePromptOptions = () => {
                    const camera = cameraWidget.value;
                    const prompts = config.prompts[camera] || defaultPrompts;
                    promptWidget.options.values = prompts;
                    if (!prompts.includes(promptWidget.value)) {
                        promptWidget.value = prompts[0];
                    }
                };

                const originalCallback = cameraWidget.callback;
                cameraWidget.callback = function (value) {
                    originalCallback?.call(this, value);
                    updatePromptOptions();
                };

                updatePromptOptions();
            };

            const onConfigure = nodeType.prototype.onConfigure;
            nodeType.prototype.onConfigure = function () {
                onConfigure?.apply(this, arguments);
                
                const cameraWidget = this.widgets.find(w => w.name === "camera");
                const promptWidget = this.widgets.find(w => w.name === "prompt");
                
                if (cameraWidget && promptWidget) {
                    const camera = cameraWidget.value;
                    const prompts = config.prompts[camera] || config.prompts[config.defaultCamera];
                    promptWidget.options.values = prompts;
                }
            };
        },
    });
}

// Register both nodes
Object.keys(NODE_CONFIGS).forEach(registerAnglePromptNode);
