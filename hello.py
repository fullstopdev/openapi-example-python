from models.com.nokia.eda.interfaces.v1alpha1 import Interface, Member, SpecModel, Metadata

def main():
    iface = Interface(
        apiVersion="interfaces.eda.nokia.com/v1alpha1",
        kind="Interface",
        metadata=Metadata(
            name="test",
            namespace="clab-vlan",
            labels={"app": "test"},
        ),
        spec=SpecModel(
            description="This is a test interface",
            enabled=True,
            members=[
                Member(
                    node="leaf1",
                    interface="ethernet-1-1",
                )
            ]
        )
    )
    print(iface.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
