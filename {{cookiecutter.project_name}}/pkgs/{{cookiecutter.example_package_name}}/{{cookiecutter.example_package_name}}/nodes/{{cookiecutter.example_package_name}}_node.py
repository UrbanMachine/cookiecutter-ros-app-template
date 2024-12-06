from typing import Any

from node_helpers.nodes import HelpfulNode
from pydantic import BaseModel
from std_msgs.msg import String
from node_helpers.spinning import create_spin_function
from rclpy.qos import qos_profile_services_default

class {{cookiecutter.example_node_name}}(HelpfulNode):

    class Parameters(BaseModel):
        # Define your ROS parameters here
        publish_value: str
        publish_hz: float

    def __init__(self, **kwargs: Any):
        super().__init__("{{cookiecutter.example_node_name}}", **kwargs)
        # Load parameters from the ROS parameter server
        self.params = self.declare_from_pydantic_model(self.Parameters, "root_config")

        # Create a publisher
        self.publisher = self.create_publisher(
            String, "example_topic", qos_profile=qos_profile_services_default
        )

        # Create a timer
        self.create_timer(1 / self.params.publish_hz, self.on_publish)


    def on_publish(self) -> None:
        msg = String()
        msg.data = self.params.publish_value
        self.publisher.publish(msg)

main = create_spin_function({{cookiecutter.example_node_name}})