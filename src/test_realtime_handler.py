import logging
from fastrtc import Stream

from reachy_mini_conversation_app.openai_realtime import OpenaiRealtimeHandler
from reachy_mini_conversation_app.tools.core_tools import ToolDependencies

logging.basicConfig(level=logging.INFO)

class DummyReachyMini: ...
class NoopMovementManager:
    def set_listening(self, v: bool): pass
    def is_idle(self) -> bool: return False

deps = ToolDependencies(
    reachy_mini=DummyReachyMini(),
    movement_manager=NoopMovementManager(),
    camera_worker=None,
    vision_manager=None,
    head_wobbler=None,
)

handler = OpenaiRealtimeHandler(deps=deps, gradio_mode=True, instance_path=".")

# IMPORTANT: set modality="audio" for a voice chat UI
stream = Stream(handler, mode="send-receive", modality="audio")

# Launch the built-in Stream UI
stream.ui.launch()
