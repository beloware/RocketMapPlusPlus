# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/telemetry/distribution.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/telemetry/distribution.proto',
  package='pogoprotos.networking.platform.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;pogoprotos/networking/platform/telemetry/distribution.proto\x12(pogoprotos.networking.platform.telemetry\"\xd5\x08\n\x0c\x44istribution\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x12\x0c\n\x04mean\x18\x02 \x01(\x02\x12 \n\x18sum_of_squared_deviation\x18\x03 \x01(\x01\x12K\n\x05range\x18\x04 \x01(\x0b\x32<.pogoprotos.networking.platform.telemetry.Distribution.Range\x12\\\n\x0e\x62ucket_options\x18\x05 \x01(\x0b\x32\x44.pogoprotos.networking.platform.telemetry.Distribution.BucketOptions\x12\x15\n\rbucket_counts\x18\x06 \x03(\x03\x1a\xfe\x03\n\rBucketOptions\x12\\\n\x0elinear_buckets\x18\x01 \x01(\x0b\x32\x44.pogoprotos.networking.platform.telemetry.Distribution.LinearBuckets\x12\x66\n\x13\x65xponential_buckets\x18\x02 \x01(\x0b\x32I.pogoprotos.networking.platform.telemetry.Distribution.ExponentialBuckets\x12`\n\x10\x65xplicit_buckets\x18\x03 \x01(\x0b\x32\x46.pogoprotos.networking.platform.telemetry.Distribution.ExplicitBuckets\x1a!\n\x0f\x45xplicitBuckets\x12\x0e\n\x06\x62ounds\x18\x01 \x03(\x03\x1aV\n\x12\x45xponentialBuckets\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x03\x12\x15\n\rgrowth_factor\x18\x02 \x01(\x02\x12\r\n\x05scale\x18\x03 \x01(\x02\x1aJ\n\rLinearBuckets\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x03\x12\r\n\x05width\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x1a!\n\x0f\x45xplicitBuckets\x12\x0e\n\x06\x62ounds\x18\x01 \x03(\x03\x1aV\n\x12\x45xponentialBuckets\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x03\x12\x15\n\rgrowth_factor\x18\x02 \x01(\x02\x12\r\n\x05scale\x18\x03 \x01(\x02\x1aJ\n\rLinearBuckets\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x03\x12\r\n\x05width\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x1a!\n\x05Range\x12\x0b\n\x03min\x18\x01 \x01(\x03\x12\x0b\n\x03max\x18\x02 \x01(\x03\"Y\n\nBucketType\x12\x08\n\x04none\x10\x00\x12\x12\n\x0elinear_buckets\x10\x01\x12\x17\n\x13\x65xponential_buckets\x10\x02\x12\x14\n\x10\x65xplicit_buckets\x10\x03\x62\x06proto3')
)



_DISTRIBUTION_BUCKETTYPE = _descriptor.EnumDescriptor(
  name='BucketType',
  full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='none', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='linear_buckets', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='exponential_buckets', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='explicit_buckets', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1126,
  serialized_end=1215,
)
_sym_db.RegisterEnumDescriptor(_DISTRIBUTION_BUCKETTYPE)


_DISTRIBUTION_BUCKETOPTIONS_EXPLICITBUCKETS = _descriptor.Descriptor(
  name='ExplicitBuckets',
  full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.ExplicitBuckets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bounds', full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.ExplicitBuckets.bounds', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=693,
  serialized_end=726,
)

_DISTRIBUTION_BUCKETOPTIONS_EXPONENTIALBUCKETS = _descriptor.Descriptor(
  name='ExponentialBuckets',
  full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.ExponentialBuckets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_finite_buckets', full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.ExponentialBuckets.num_finite_buckets', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='growth_factor', full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.ExponentialBuckets.growth_factor', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.ExponentialBuckets.scale', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=728,
  serialized_end=814,
)

_DISTRIBUTION_BUCKETOPTIONS_LINEARBUCKETS = _descriptor.Descriptor(
  name='LinearBuckets',
  full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.LinearBuckets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_finite_buckets', full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.LinearBuckets.num_finite_buckets', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.LinearBuckets.width', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.LinearBuckets.offset', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=816,
  serialized_end=890,
)

_DISTRIBUTION_BUCKETOPTIONS = _descriptor.Descriptor(
  name='BucketOptions',
  full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linear_buckets', full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.linear_buckets', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exponential_buckets', full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.exponential_buckets', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='explicit_buckets', full_name='pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.explicit_buckets', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DISTRIBUTION_BUCKETOPTIONS_EXPLICITBUCKETS, _DISTRIBUTION_BUCKETOPTIONS_EXPONENTIALBUCKETS, _DISTRIBUTION_BUCKETOPTIONS_LINEARBUCKETS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=890,
)

_DISTRIBUTION_EXPLICITBUCKETS = _descriptor.Descriptor(
  name='ExplicitBuckets',
  full_name='pogoprotos.networking.platform.telemetry.Distribution.ExplicitBuckets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bounds', full_name='pogoprotos.networking.platform.telemetry.Distribution.ExplicitBuckets.bounds', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=693,
  serialized_end=726,
)

_DISTRIBUTION_EXPONENTIALBUCKETS = _descriptor.Descriptor(
  name='ExponentialBuckets',
  full_name='pogoprotos.networking.platform.telemetry.Distribution.ExponentialBuckets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_finite_buckets', full_name='pogoprotos.networking.platform.telemetry.Distribution.ExponentialBuckets.num_finite_buckets', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='growth_factor', full_name='pogoprotos.networking.platform.telemetry.Distribution.ExponentialBuckets.growth_factor', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='pogoprotos.networking.platform.telemetry.Distribution.ExponentialBuckets.scale', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=728,
  serialized_end=814,
)

_DISTRIBUTION_LINEARBUCKETS = _descriptor.Descriptor(
  name='LinearBuckets',
  full_name='pogoprotos.networking.platform.telemetry.Distribution.LinearBuckets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_finite_buckets', full_name='pogoprotos.networking.platform.telemetry.Distribution.LinearBuckets.num_finite_buckets', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='pogoprotos.networking.platform.telemetry.Distribution.LinearBuckets.width', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='pogoprotos.networking.platform.telemetry.Distribution.LinearBuckets.offset', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=816,
  serialized_end=890,
)

_DISTRIBUTION_RANGE = _descriptor.Descriptor(
  name='Range',
  full_name='pogoprotos.networking.platform.telemetry.Distribution.Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='pogoprotos.networking.platform.telemetry.Distribution.Range.min', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='pogoprotos.networking.platform.telemetry.Distribution.Range.max', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=1091,
  serialized_end=1124,
)

_DISTRIBUTION = _descriptor.Descriptor(
  name='Distribution',
  full_name='pogoprotos.networking.platform.telemetry.Distribution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='pogoprotos.networking.platform.telemetry.Distribution.count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean', full_name='pogoprotos.networking.platform.telemetry.Distribution.mean', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sum_of_squared_deviation', full_name='pogoprotos.networking.platform.telemetry.Distribution.sum_of_squared_deviation', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='pogoprotos.networking.platform.telemetry.Distribution.range', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket_options', full_name='pogoprotos.networking.platform.telemetry.Distribution.bucket_options', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket_counts', full_name='pogoprotos.networking.platform.telemetry.Distribution.bucket_counts', index=5,
      number=6, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DISTRIBUTION_BUCKETOPTIONS, _DISTRIBUTION_EXPLICITBUCKETS, _DISTRIBUTION_EXPONENTIALBUCKETS, _DISTRIBUTION_LINEARBUCKETS, _DISTRIBUTION_RANGE, ],
  enum_types=[
    _DISTRIBUTION_BUCKETTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=1215,
)

_DISTRIBUTION_BUCKETOPTIONS_EXPLICITBUCKETS.containing_type = _DISTRIBUTION_BUCKETOPTIONS
_DISTRIBUTION_BUCKETOPTIONS_EXPONENTIALBUCKETS.containing_type = _DISTRIBUTION_BUCKETOPTIONS
_DISTRIBUTION_BUCKETOPTIONS_LINEARBUCKETS.containing_type = _DISTRIBUTION_BUCKETOPTIONS
_DISTRIBUTION_BUCKETOPTIONS.fields_by_name['linear_buckets'].message_type = _DISTRIBUTION_LINEARBUCKETS
_DISTRIBUTION_BUCKETOPTIONS.fields_by_name['exponential_buckets'].message_type = _DISTRIBUTION_EXPONENTIALBUCKETS
_DISTRIBUTION_BUCKETOPTIONS.fields_by_name['explicit_buckets'].message_type = _DISTRIBUTION_EXPLICITBUCKETS
_DISTRIBUTION_BUCKETOPTIONS.containing_type = _DISTRIBUTION
_DISTRIBUTION_EXPLICITBUCKETS.containing_type = _DISTRIBUTION
_DISTRIBUTION_EXPONENTIALBUCKETS.containing_type = _DISTRIBUTION
_DISTRIBUTION_LINEARBUCKETS.containing_type = _DISTRIBUTION
_DISTRIBUTION_RANGE.containing_type = _DISTRIBUTION
_DISTRIBUTION.fields_by_name['range'].message_type = _DISTRIBUTION_RANGE
_DISTRIBUTION.fields_by_name['bucket_options'].message_type = _DISTRIBUTION_BUCKETOPTIONS
_DISTRIBUTION_BUCKETTYPE.containing_type = _DISTRIBUTION
DESCRIPTOR.message_types_by_name['Distribution'] = _DISTRIBUTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Distribution = _reflection.GeneratedProtocolMessageType('Distribution', (_message.Message,), dict(

  BucketOptions = _reflection.GeneratedProtocolMessageType('BucketOptions', (_message.Message,), dict(

    ExplicitBuckets = _reflection.GeneratedProtocolMessageType('ExplicitBuckets', (_message.Message,), dict(
      DESCRIPTOR = _DISTRIBUTION_BUCKETOPTIONS_EXPLICITBUCKETS,
      __module__ = 'pogoprotos.networking.platform.telemetry.distribution_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.ExplicitBuckets)
      ))
    ,

    ExponentialBuckets = _reflection.GeneratedProtocolMessageType('ExponentialBuckets', (_message.Message,), dict(
      DESCRIPTOR = _DISTRIBUTION_BUCKETOPTIONS_EXPONENTIALBUCKETS,
      __module__ = 'pogoprotos.networking.platform.telemetry.distribution_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.ExponentialBuckets)
      ))
    ,

    LinearBuckets = _reflection.GeneratedProtocolMessageType('LinearBuckets', (_message.Message,), dict(
      DESCRIPTOR = _DISTRIBUTION_BUCKETOPTIONS_LINEARBUCKETS,
      __module__ = 'pogoprotos.networking.platform.telemetry.distribution_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.telemetry.Distribution.BucketOptions.LinearBuckets)
      ))
    ,
    DESCRIPTOR = _DISTRIBUTION_BUCKETOPTIONS,
    __module__ = 'pogoprotos.networking.platform.telemetry.distribution_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.telemetry.Distribution.BucketOptions)
    ))
  ,

  ExplicitBuckets = _reflection.GeneratedProtocolMessageType('ExplicitBuckets', (_message.Message,), dict(
    DESCRIPTOR = _DISTRIBUTION_EXPLICITBUCKETS,
    __module__ = 'pogoprotos.networking.platform.telemetry.distribution_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.telemetry.Distribution.ExplicitBuckets)
    ))
  ,

  ExponentialBuckets = _reflection.GeneratedProtocolMessageType('ExponentialBuckets', (_message.Message,), dict(
    DESCRIPTOR = _DISTRIBUTION_EXPONENTIALBUCKETS,
    __module__ = 'pogoprotos.networking.platform.telemetry.distribution_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.telemetry.Distribution.ExponentialBuckets)
    ))
  ,

  LinearBuckets = _reflection.GeneratedProtocolMessageType('LinearBuckets', (_message.Message,), dict(
    DESCRIPTOR = _DISTRIBUTION_LINEARBUCKETS,
    __module__ = 'pogoprotos.networking.platform.telemetry.distribution_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.telemetry.Distribution.LinearBuckets)
    ))
  ,

  Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), dict(
    DESCRIPTOR = _DISTRIBUTION_RANGE,
    __module__ = 'pogoprotos.networking.platform.telemetry.distribution_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.telemetry.Distribution.Range)
    ))
  ,
  DESCRIPTOR = _DISTRIBUTION,
  __module__ = 'pogoprotos.networking.platform.telemetry.distribution_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.telemetry.Distribution)
  ))
_sym_db.RegisterMessage(Distribution)
_sym_db.RegisterMessage(Distribution.BucketOptions)
_sym_db.RegisterMessage(Distribution.BucketOptions.ExplicitBuckets)
_sym_db.RegisterMessage(Distribution.BucketOptions.ExponentialBuckets)
_sym_db.RegisterMessage(Distribution.BucketOptions.LinearBuckets)
_sym_db.RegisterMessage(Distribution.ExplicitBuckets)
_sym_db.RegisterMessage(Distribution.ExponentialBuckets)
_sym_db.RegisterMessage(Distribution.LinearBuckets)
_sym_db.RegisterMessage(Distribution.Range)


# @@protoc_insertion_point(module_scope)
