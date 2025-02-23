generate:
	python -m grpc_tools.protoc -I src/proto --python_out=src/proto/gen --grpc_python_out=src/proto/gen src/proto/detect.proto



