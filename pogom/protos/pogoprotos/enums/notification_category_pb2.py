# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/notification_category.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/notification_category.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,pogoprotos/enums/notification_category.proto\x12\x10pogoprotos.enums*\x8d\x03\n\x14NotificationCategory\x12\x1e\n\x1aUNSET_NotificationCategory\x10\x00\x12\x0f\n\x0bGYM_REMOVAL\x10\x01\x12\x12\n\x0ePOKEMON_HUNGRY\x10\x02\x12\x0f\n\x0bPOKEMON_WON\x10\x03\x12\x19\n\x15\x45XCLUSIVE_RAID_INVITE\x10\x04\x12\x1f\n\x1b\x45XCLUSIVE_RAID_CANCELLATION\x10\x05\x12\x14\n\x10GIFTBOX_INCOMING\x10\x06\x12\x15\n\x11GIFTBOX_DELIVERED\x10\x07\x12\x1f\n\x1b\x46RIENDSHIP_MILESTONE_REWARD\x10\x08\x12#\n\x1fGYM_BATTLE_FRIENDSHIP_INCREMENT\x10\t\x12 \n\x1cSHARED_EXCLUSIVE_RAID_INVITE\x10\n\x12\x14\n\x10\x42GMODE_EGG_HATCH\x10\x0b\x12\x16\n\x12\x42GMODE_BUDDY_CANDY\x10\x0c\x12 \n\x1c\x42GMODE_WEEKLY_FITNESS_REPORT\x10\rb\x06proto3')
)

_NOTIFICATIONCATEGORY = _descriptor.EnumDescriptor(
  name='NotificationCategory',
  full_name='pogoprotos.enums.NotificationCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_NotificationCategory', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_REMOVAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_HUNGRY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_WON', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCLUSIVE_RAID_INVITE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCLUSIVE_RAID_CANCELLATION', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIFTBOX_INCOMING', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIFTBOX_DELIVERED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIENDSHIP_MILESTONE_REWARD', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BATTLE_FRIENDSHIP_INCREMENT', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARED_EXCLUSIVE_RAID_INVITE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_EGG_HATCH', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_BUDDY_CANDY', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_WEEKLY_FITNESS_REPORT', index=13, number=13,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=67,
  serialized_end=464,
)
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONCATEGORY)

NotificationCategory = enum_type_wrapper.EnumTypeWrapper(_NOTIFICATIONCATEGORY)
UNSET_NotificationCategory = 0
GYM_REMOVAL = 1
POKEMON_HUNGRY = 2
POKEMON_WON = 3
EXCLUSIVE_RAID_INVITE = 4
EXCLUSIVE_RAID_CANCELLATION = 5
GIFTBOX_INCOMING = 6
GIFTBOX_DELIVERED = 7
FRIENDSHIP_MILESTONE_REWARD = 8
GYM_BATTLE_FRIENDSHIP_INCREMENT = 9
SHARED_EXCLUSIVE_RAID_INVITE = 10
BGMODE_EGG_HATCH = 11
BGMODE_BUDDY_CANDY = 12
BGMODE_WEEKLY_FITNESS_REPORT = 13


DESCRIPTOR.enum_types_by_name['NotificationCategory'] = _NOTIFICATIONCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
