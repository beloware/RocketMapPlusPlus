# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/applied_items.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import applied_item_pb2 as pogoprotos_dot_inventory_dot_applied__item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/applied_items.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/inventory/applied_items.proto\x12\x14pogoprotos.inventory\x1a\'pogoprotos/inventory/applied_item.proto\"?\n\x0c\x41ppliedItems\x12/\n\x04item\x18\x04 \x03(\x0b\x32!.pogoprotos.inventory.AppliedItemb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_applied__item__pb2.DESCRIPTOR,])




_APPLIEDITEMS = _descriptor.Descriptor(
  name='AppliedItems',
  full_name='pogoprotos.inventory.AppliedItems',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='pogoprotos.inventory.AppliedItems.item', index=0,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=107,
  serialized_end=170,
)

_APPLIEDITEMS.fields_by_name['item'].message_type = pogoprotos_dot_inventory_dot_applied__item__pb2._APPLIEDITEM
DESCRIPTOR.message_types_by_name['AppliedItems'] = _APPLIEDITEMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppliedItems = _reflection.GeneratedProtocolMessageType('AppliedItems', (_message.Message,), dict(
  DESCRIPTOR = _APPLIEDITEMS,
  __module__ = 'pogoprotos.inventory.applied_items_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.AppliedItems)
  ))
_sym_db.RegisterMessage(AppliedItems)


# @@protoc_insertion_point(module_scope)
