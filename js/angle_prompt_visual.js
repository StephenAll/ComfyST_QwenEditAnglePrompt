import { app } from "../../scripts/app.js";
import { IMAGE_DATA } from "./angle_prompt_images.js";

function getCurrentLanguage() {
    return app.ui?.settings?.getSettingValue?.('Comfy.Locale') || 'en';
}

const UI_LABELS = {
    en: {
        groups: ["Close-up", "Medium Shot", "Wide Shot"],
        selectAll: "Select All",
        clear: "Clear",
        selected: "Selected"
    },
    zh: {
        groups: ["特写镜头组", "中景镜头组", "全景镜头组"],
        selectAll: "全选",
        clear: "清除",
        selected: "已选择"
    }
};

const PROMPTS_EN = [
    "front view low-angle shot close-up", "front-right quarter view low-angle shot close-up",
    "right side view low-angle shot close-up", "back-right quarter view low-angle shot close-up",
    "back view low-angle shot close-up", "back-left quarter view low-angle shot close-up",
    "left side view low-angle shot close-up", "front-left quarter view low-angle shot close-up",
    "front view eye-level shot close-up", "front-right quarter view eye-level shot close-up",
    "right side view eye-level shot close-up", "back-right quarter view eye-level shot close-up",
    "back view eye-level shot close-up", "back-left quarter view eye-level shot close-up",
    "left side view eye-level shot close-up", "front-left quarter view eye-level shot close-up",
    "front view elevated shot close-up", "front-right quarter view elevated shot close-up",
    "right side view elevated shot close-up", "back-right quarter view elevated shot close-up",
    "back view elevated shot close-up", "back-left quarter view elevated shot close-up",
    "left side view elevated shot close-up", "front-left quarter view elevated shot close-up",
    "front view high-angle shot close-up", "front-right quarter view high-angle shot close-up",
    "right side view high-angle shot close-up", "back-right quarter view high-angle shot close-up",
    "back view high-angle shot close-up", "back-left quarter view high-angle shot close-up",
    "left side view high-angle shot close-up", "front-left quarter view high-angle shot close-up",
    "front view low-angle shot medium shot", "front-right quarter view low-angle shot medium shot",
    "right side view low-angle shot medium shot", "back-right quarter view low-angle shot medium shot",
    "back view low-angle shot medium shot", "back-left quarter view low-angle shot medium shot",
    "left side view low-angle shot medium shot", "front-left quarter view low-angle shot medium shot",
    "front view eye-level shot medium shot", "front-right quarter view eye-level shot medium shot",
    "right side view eye-level shot medium shot", "back-right quarter view eye-level shot medium shot",
    "back view eye-level shot medium shot", "back-left quarter view eye-level shot medium shot",
    "left side view eye-level shot medium shot", "front-left quarter view eye-level shot medium shot",
    "front view elevated shot medium shot", "front-right quarter view elevated shot medium shot",
    "right side view elevated shot medium shot", "back-right quarter view elevated shot medium shot",
    "back view elevated shot medium shot", "back-left quarter view elevated shot medium shot",
    "left side view elevated shot medium shot", "front-left quarter view elevated shot medium shot",
    "front view high-angle shot medium shot", "front-right quarter view high-angle shot medium shot",
    "right side view high-angle shot medium shot", "back-right quarter view high-angle shot medium shot",
    "back view high-angle shot medium shot", "back-left quarter view high-angle shot medium shot",
    "left side view high-angle shot medium shot", "front-left quarter view high-angle shot medium shot",
    "front view low-angle shot wide shot", "front-right quarter view low-angle shot wide shot",
    "right side view low-angle shot wide shot", "back-right quarter view low-angle shot wide shot",
    "back view low-angle shot wide shot", "back-left quarter view low-angle shot wide shot",
    "left side view low-angle shot wide shot", "front-left quarter view low-angle shot wide shot",
    "front view eye-level shot wide shot", "front-right quarter view eye-level shot wide shot",
    "right side view eye-level shot wide shot", "back-right quarter view eye-level shot wide shot",
    "back view eye-level shot wide shot", "back-left quarter view eye-level shot wide shot",
    "left side view eye-level shot wide shot", "front-left quarter view eye-level shot wide shot",
    "front view elevated shot wide shot", "front-right quarter view elevated shot wide shot",
    "right side view elevated shot wide shot", "back-right quarter view elevated shot wide shot",
    "back view elevated shot wide shot", "back-left quarter view elevated shot wide shot",
    "left side view elevated shot wide shot", "front-left quarter view elevated shot wide shot",
    "front view high-angle shot wide shot", "front-right quarter view high-angle shot wide shot",
    "right side view high-angle shot wide shot", "back-right quarter view high-angle shot wide shot",
    "back view high-angle shot wide shot", "back-left quarter view high-angle shot wide shot",
    "left side view high-angle shot wide shot", "front-left quarter view high-angle shot wide shot",
];

const PROMPTS_CN = [
    "正面低仰角特写", "右前方低仰角特写", "右侧面低仰角特写", "右后方低仰角特写",
    "背面低仰角特写", "左后方低仰角特写", "左侧面低仰角特写", "左前方低仰角特写",
    "正面平视特写", "右前方平视特写", "右侧面平视特写", "右后方平视特写",
    "背面平视特写", "左后方平视特写", "左侧面平视特写", "左前方平视特写",
    "正面高位特写", "右前方高位特写", "右侧面高位特写", "右后方高位特写",
    "背面高位特写", "左后方高位特写", "左侧面高位特写", "左前方高位特写",
    "正面高角度俯拍特写", "右前方高角度俯拍特写", "右侧面高角度俯拍特写", "右后方高角度俯拍特写",
    "背面高角度俯拍特写", "左后方高角度俯拍特写", "左侧面高角度俯拍特写", "左前方高角度俯拍特写",
    "正面低仰角中景", "右前方低仰角中景", "右侧面低仰角中景", "右后方低仰角中景",
    "背面低仰角中景", "左后方低仰角中景", "左侧面低仰角中景", "左前方低仰角中景",
    "正面平视中景", "右前方平视中景", "右侧面平视中景", "右后方平视中景",
    "背面平视中景", "左后方平视中景", "左侧面平视中景", "左前方平视中景",
    "正面高位中景", "右前方高位中景", "右侧面高位中景", "右后方高位中景",
    "背面高位中景", "左后方高位中景", "左侧面高位中景", "左前方高位中景",
    "正面高角度俯拍中景", "右前方高角度俯拍中景", "右侧面高角度俯拍中景", "右后方高角度俯拍中景",
    "背面高角度俯拍中景", "左后方高角度俯拍中景", "左侧面高角度俯拍中景", "左前方高角度俯拍中景",
    "正面低仰角全景", "右前方低仰角全景", "右侧面低仰角全景", "右后方低仰角全景",
    "背面低仰角全景", "左后方低仰角全景", "左侧面低仰角全景", "左前方低仰角全景",
    "正面平视全景", "右前方平视全景", "右侧面平视全景", "右后方平视全景",
    "背面平视全景", "左后方平视全景", "左侧面平视全景", "左前方平视全景",
    "正面高位全景", "右前方高位全景", "右侧面高位全景", "右后方高位全景",
    "背面高位全景", "左后方高位全景", "左侧面高位全景", "左前方高位全景",
    "正面高角度俯拍全景", "右前方高角度俯拍全景", "右侧面高角度俯拍全景", "右后方高角度俯拍全景",
    "背面高角度俯拍全景", "左后方高角度俯拍全景", "左侧面高角度俯拍全景", "左前方高角度俯拍全景",
];

function getLabels() {
    const lang = getCurrentLanguage();
    return UI_LABELS[lang] || UI_LABELS.en;
}

function getTooltipPrompts() {
    const lang = getCurrentLanguage();
    return lang === 'zh' ? PROMPTS_CN : PROMPTS_EN;
}

app.registerExtension({
    name: "QwenAnglePromptVisual",
    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== "QwenAnglePromptVisual") return;

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            onNodeCreated?.apply(this, arguments);

            const node = this;
            node.selectedIndices = new Set();
            node.imageElements = [];
            node.currentTab = 0;

            const selectedIndicesWidget = node.widgets.find(w => w.name === "selected_indices");
            const labels = getLabels();
            const tooltipPrompts = getTooltipPrompts();

            const container = document.createElement("div");
            container.style.cssText = "display:flex; flex-direction:column; gap:8px; padding:0; background:#1a1a1a; border-radius:4px;";

            const tabContainer = document.createElement("div");
            tabContainer.style.cssText = "display:flex; gap:4px;";
            
            const tabs = [];
            for (let i = 0; i < 3; i++) {
                const tab = document.createElement("button");
                tab.textContent = `${labels.groups[i]} (0)`;
                tab.style.cssText = "flex:1; padding:6px; border:none; border-radius:4px; cursor:pointer; font-size:12px;";
                tab.style.background = i === 0 ? "#4a9eff" : "#333";
                tab.style.color = "#fff";
                tab.onclick = () => switchTab(i);
                tabContainer.appendChild(tab);
                tabs.push(tab);
            }
            container.appendChild(tabContainer);

            const actionContainer = document.createElement("div");
            actionContainer.style.cssText = "display:flex; gap:4px;";
            
            const selectAllBtn = document.createElement("button");
            selectAllBtn.textContent = labels.selectAll;
            selectAllBtn.style.cssText = "flex:1; padding:4px; border:none; border-radius:4px; cursor:pointer; background:#555; color:#fff; font-size:11px;";
            selectAllBtn.onclick = () => selectAllInTab();
            
            const clearBtn = document.createElement("button");
            clearBtn.textContent = labels.clear;
            clearBtn.style.cssText = "flex:1; padding:4px; border:none; border-radius:4px; cursor:pointer; background:#555; color:#fff; font-size:11px;";
            clearBtn.onclick = () => clearSelection();
            
            actionContainer.appendChild(selectAllBtn);
            actionContainer.appendChild(clearBtn);
            container.appendChild(actionContainer);

            const gridContainer = document.createElement("div");
            gridContainer.style.cssText = "display:grid; grid-template-columns:repeat(8,1fr); gap:4px;";

            for (let i = 0; i < 96; i++) {
                const wrapper = document.createElement("div");
                wrapper.style.cssText = "position:relative; aspect-ratio:3/4; cursor:pointer; border:2px solid transparent; border-radius:4px; overflow:hidden;";
                wrapper.dataset.index = i;
                wrapper.style.display = (i < 32) ? "block" : "none";

                const img = document.createElement("img");
                img.src = IMAGE_DATA[i];
                img.style.cssText = "width:100%; height:100%; object-fit:cover;";
                img.title = tooltipPrompts[i];
                img.onerror = () => { img.style.background = "#333"; };
                
                wrapper.appendChild(img);
                wrapper.onclick = () => toggleSelection(i);
                
                gridContainer.appendChild(wrapper);
                node.imageElements.push({ wrapper, img });
            }
            container.appendChild(gridContainer);

            const countLabel = document.createElement("div");
            countLabel.style.cssText = "text-align:center; color:#888; font-size:11px;";
            countLabel.textContent = `${labels.selected}: 0`;
            container.appendChild(countLabel);

            // Add DOM widget
            const widget = node.addDOMWidget("image_grid", "div", container, {
                serialize: false,
                hideOnZoom: false,
            });
            widget.computeSize = () => [node.size[0], 420];

            // Functions
            function switchTab(tabIndex) {
                node.currentTab = tabIndex;
                tabs.forEach((t, i) => {
                    t.style.background = i === tabIndex ? "#4a9eff" : "#333";
                });
                const start = tabIndex * 32;
                const end = start + 32;
                node.imageElements.forEach((el, i) => {
                    el.wrapper.style.display = (i >= start && i < end) ? "block" : "none";
                });
            }

            function toggleSelection(index) {
                if (node.selectedIndices.has(index)) {
                    node.selectedIndices.delete(index);
                    node.imageElements[index].wrapper.style.borderColor = "transparent";
                } else {
                    node.selectedIndices.add(index);
                    node.imageElements[index].wrapper.style.borderColor = "#4a9eff";
                }
                updateSelectedIndices();
            }

            function selectAllInTab() {
                const start = node.currentTab * 32;
                const end = start + 32;
                for (let i = start; i < end; i++) {
                    node.selectedIndices.add(i);
                    node.imageElements[i].wrapper.style.borderColor = "#4a9eff";
                }
                updateSelectedIndices();
            }

            function clearSelection() {
                node.selectedIndices.clear();
                node.imageElements.forEach(el => {
                    el.wrapper.style.borderColor = "transparent";
                });
                updateSelectedIndices();
            }

            function updateSelectedIndices() {
                const indices = Array.from(node.selectedIndices).sort((a, b) => a - b);
                if (selectedIndicesWidget) {
                    selectedIndicesWidget.value = indices.join(",");
                }
                const labels = getLabels();
                countLabel.textContent = `${labels.selected}: ${indices.length}`;
                
                for (let t = 0; t < 3; t++) {
                    const start = t * 32;
                    const end = start + 32;
                    const count = indices.filter(i => i >= start && i < end).length;
                    tabs[t].textContent = `${labels.groups[t]} (${count})`;
                }
            }

            node.onConfigure = function(info) {
                if (info.widgets_values) {
                    const idx = node.widgets.findIndex(w => w.name === "selected_indices");
                    if (idx >= 0 && info.widgets_values[idx]) {
                        const indices = info.widgets_values[idx].split(",").filter(s => s).map(Number);
                        node.selectedIndices = new Set(indices);
                        node.imageElements.forEach((el, i) => {
                            el.wrapper.style.borderColor = node.selectedIndices.has(i) ? "#4a9eff" : "transparent";
                        });
                        updateSelectedIndices();
                    }
                }
            };
        };
    },
});
