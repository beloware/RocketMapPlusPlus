# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/inventory_item.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import inventory_item_data_pb2 as pogoprotos_dot_inventory_dot_inventory__item__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/inventory_item.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)pogoprotos/inventory/inventory_item.proto\x12\x14pogoprotos.inventory\x1a.pogoprotos/inventory/inventory_item_data.proto\"\xde\x01\n\rInventoryItem\x12\x1d\n\x15modified_timestamp_ms\x18\x01 \x01(\x03\x12\x45\n\x0c\x64\x65leted_item\x18\x02 \x01(\x0b\x32/.pogoprotos.inventory.InventoryItem.DeletedItem\x12\x44\n\x13inventory_item_data\x18\x03 \x01(\x0b\x32\'.pogoprotos.inventory.InventoryItemData\x1a!\n\x0b\x44\x65letedItem\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_inventory__item__data__pb2.DESCRIPTOR,])




_INVENTORYITEM_DELETEDITEM = _descriptor.Descriptor(
  name='DeletedItem',
  full_name='pogoprotos.inventory.InventoryItem.DeletedItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.inventory.InventoryItem.DeletedItem.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
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
  serialized_start=305,
  serialized_end=338,
)

_INVENTORYITEM = _descriptor.Descriptor(
  name='InventoryItem',
  full_name='pogoprotos.inventory.InventoryItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modified_timestamp_ms', full_name='pogoprotos.inventory.InventoryItem.modified_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleted_item', full_name='pogoprotos.inventory.InventoryItem.deleted_item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inventory_item_data', full_name='pogoprotos.inventory.InventoryItem.inventory_item_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INVENTORYITEM_DELETEDITEM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=338,
)

_INVENTORYITEM_DELETEDITEM.containing_type = _INVENTORYITEM
_INVENTORYITEM.fields_by_name['deleted_item'].message_type = _INVENTORYITEM_DELETEDITEM
_INVENTORYITEM.fields_by_name['inventory_item_data'].message_type = pogoprotos_dot_inventory_dot_inventory__item__data__pb2._INVENTORYITEMDATA
DESCRIPTOR.message_types_by_name['InventoryItem'] = _INVENTORYITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InventoryItem = _reflection.GeneratedProtocolMessageType('InventoryItem', (_message.Message,), dict(

  DeletedItem = _reflection.GeneratedProtocolMessageType('DeletedItem', (_message.Message,), dict(
    DESCRIPTOR = _INVENTORYITEM_DELETEDITEM,
    __module__ = 'pogoprotos.inventory.inventory_item_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.inventory.InventoryItem.DeletedItem)
    ))
  ,
  DESCRIPTOR = _INVENTORYITEM,
  __module__ = 'pogoprotos.inventory.inventory_item_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.InventoryItem)
  ))
_sym_db.RegisterMessage(InventoryItem)
_sym_db.RegisterMessage(InventoryItem.DeletedItem)


# @@protoc_insertion_point(module_scope)
