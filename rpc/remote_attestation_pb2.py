# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote_attestation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ndarray_pb2 as ndarray__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='remote_attestation.proto',
  package='remote_attestation',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18remote_attestation.proto\x12\x12remote_attestation\x1a\rndarray.proto\"\x18\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x96\x01\n\x06Report\x12+\n\x07pem_key\x18\x01 \x01(\x0b\x32\x1a.numproto.protobuf.NDArray\x12\x10\n\x08key_size\x18\x02 \x01(\r\x12\x31\n\rremote_report\x18\x03 \x01(\x0b\x32\x1a.numproto.protobuf.NDArray\x12\x1a\n\x12remote_report_size\x18\x04 \x01(\r\"\x91\x01\n\x0c\x44\x61taMetadata\x12/\n\x0b\x65nc_sym_key\x18\x01 \x01(\x0b\x32\x1a.numproto.protobuf.NDArray\x12\x10\n\x08key_size\x18\x02 \x01(\r\x12-\n\tsignature\x18\x03 \x01(\x0b\x32\x1a.numproto.protobuf.NDArray\x12\x0f\n\x07sig_len\x18\x04 \x01(\r\"a\n\x0bPredictions\x12/\n\x0bpredictions\x18\x01 \x01(\x0b\x32\x1a.numproto.protobuf.NDArray\x12\x11\n\tnum_preds\x18\x02 \x01(\r\x12\x0e\n\x06status\x18\x03 \x01(\r2\xf8\x01\n\x11RemoteAttestation\x12J\n\x0eGetAttestation\x12\x1a.remote_attestation.Status\x1a\x1a.remote_attestation.Report\"\x00\x12I\n\x07SendKey\x12 .remote_attestation.DataMetadata\x1a\x1a.remote_attestation.Status\"\x00\x12L\n\x0bSignalStart\x12\x1a.remote_attestation.Status\x1a\x1f.remote_attestation.Predictions\"\x00\x62\x06proto3')
  ,
  dependencies=[ndarray__pb2.DESCRIPTOR,])




_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='remote_attestation.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='remote_attestation.Status.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=87,
)


_REPORT = _descriptor.Descriptor(
  name='Report',
  full_name='remote_attestation.Report',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pem_key', full_name='remote_attestation.Report.pem_key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_size', full_name='remote_attestation.Report.key_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_report', full_name='remote_attestation.Report.remote_report', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_report_size', full_name='remote_attestation.Report.remote_report_size', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=240,
)


_DATAMETADATA = _descriptor.Descriptor(
  name='DataMetadata',
  full_name='remote_attestation.DataMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enc_sym_key', full_name='remote_attestation.DataMetadata.enc_sym_key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_size', full_name='remote_attestation.DataMetadata.key_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='remote_attestation.DataMetadata.signature', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sig_len', full_name='remote_attestation.DataMetadata.sig_len', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=388,
)


_PREDICTIONS = _descriptor.Descriptor(
  name='Predictions',
  full_name='remote_attestation.Predictions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predictions', full_name='remote_attestation.Predictions.predictions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_preds', full_name='remote_attestation.Predictions.num_preds', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='remote_attestation.Predictions.status', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=487,
)

_REPORT.fields_by_name['pem_key'].message_type = ndarray__pb2._NDARRAY
_REPORT.fields_by_name['remote_report'].message_type = ndarray__pb2._NDARRAY
_DATAMETADATA.fields_by_name['enc_sym_key'].message_type = ndarray__pb2._NDARRAY
_DATAMETADATA.fields_by_name['signature'].message_type = ndarray__pb2._NDARRAY
_PREDICTIONS.fields_by_name['predictions'].message_type = ndarray__pb2._NDARRAY
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['Report'] = _REPORT
DESCRIPTOR.message_types_by_name['DataMetadata'] = _DATAMETADATA
DESCRIPTOR.message_types_by_name['Predictions'] = _PREDICTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'remote_attestation_pb2'
  # @@protoc_insertion_point(class_scope:remote_attestation.Status)
  })
_sym_db.RegisterMessage(Status)

Report = _reflection.GeneratedProtocolMessageType('Report', (_message.Message,), {
  'DESCRIPTOR' : _REPORT,
  '__module__' : 'remote_attestation_pb2'
  # @@protoc_insertion_point(class_scope:remote_attestation.Report)
  })
_sym_db.RegisterMessage(Report)

DataMetadata = _reflection.GeneratedProtocolMessageType('DataMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DATAMETADATA,
  '__module__' : 'remote_attestation_pb2'
  # @@protoc_insertion_point(class_scope:remote_attestation.DataMetadata)
  })
_sym_db.RegisterMessage(DataMetadata)

Predictions = _reflection.GeneratedProtocolMessageType('Predictions', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONS,
  '__module__' : 'remote_attestation_pb2'
  # @@protoc_insertion_point(class_scope:remote_attestation.Predictions)
  })
_sym_db.RegisterMessage(Predictions)



_REMOTEATTESTATION = _descriptor.ServiceDescriptor(
  name='RemoteAttestation',
  full_name='remote_attestation.RemoteAttestation',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=490,
  serialized_end=738,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAttestation',
    full_name='remote_attestation.RemoteAttestation.GetAttestation',
    index=0,
    containing_service=None,
    input_type=_STATUS,
    output_type=_REPORT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendKey',
    full_name='remote_attestation.RemoteAttestation.SendKey',
    index=1,
    containing_service=None,
    input_type=_DATAMETADATA,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SignalStart',
    full_name='remote_attestation.RemoteAttestation.SignalStart',
    index=2,
    containing_service=None,
    input_type=_STATUS,
    output_type=_PREDICTIONS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REMOTEATTESTATION)

DESCRIPTOR.services_by_name['RemoteAttestation'] = _REMOTEATTESTATION

# @@protoc_insertion_point(module_scope)
