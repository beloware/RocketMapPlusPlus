# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/map_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/map_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&pogoprotos/settings/map_settings.proto\x12\x13pogoprotos.settings\"\xf7\x02\n\x0bMapSettings\x12\x1d\n\x15pokemon_visible_range\x18\x01 \x01(\x01\x12\x1d\n\x15poke_nav_range_meters\x18\x02 \x01(\x01\x12\x1e\n\x16\x65ncounter_range_meters\x18\x03 \x01(\x01\x12+\n#get_map_objects_min_refresh_seconds\x18\x04 \x01(\x02\x12+\n#get_map_objects_max_refresh_seconds\x18\x05 \x01(\x02\x12+\n#get_map_objects_min_distance_meters\x18\x06 \x01(\x02\x12\x1b\n\x13google_maps_api_key\x18\x07 \x01(\t\x12!\n\x19min_nearby_hide_sightings\x18\x08 \x01(\x05\x12\x1e\n\x16\x65nable_special_weather\x18\t \x01(\x08\x12#\n\x1bspecial_weather_probability\x18\n \x01(\x02\x62\x06proto3')
)




_MAPSETTINGS = _descriptor.Descriptor(
  name='MapSettings',
  full_name='pogoprotos.settings.MapSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_visible_range', full_name='pogoprotos.settings.MapSettings.pokemon_visible_range', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poke_nav_range_meters', full_name='pogoprotos.settings.MapSettings.poke_nav_range_meters', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encounter_range_meters', full_name='pogoprotos.settings.MapSettings.encounter_range_meters', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_map_objects_min_refresh_seconds', full_name='pogoprotos.settings.MapSettings.get_map_objects_min_refresh_seconds', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_map_objects_max_refresh_seconds', full_name='pogoprotos.settings.MapSettings.get_map_objects_max_refresh_seconds', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_map_objects_min_distance_meters', full_name='pogoprotos.settings.MapSettings.get_map_objects_min_distance_meters', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='google_maps_api_key', full_name='pogoprotos.settings.MapSettings.google_maps_api_key', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_nearby_hide_sightings', full_name='pogoprotos.settings.MapSettings.min_nearby_hide_sightings', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_special_weather', full_name='pogoprotos.settings.MapSettings.enable_special_weather', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='special_weather_probability', full_name='pogoprotos.settings.MapSettings.special_weather_probability', index=9,
      number=10, type=2, cpp_type=6, label=1,
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
  serialized_start=64,
  serialized_end=439,
)

DESCRIPTOR.message_types_by_name['MapSettings'] = _MAPSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MapSettings = _reflection.GeneratedProtocolMessageType('MapSettings', (_message.Message,), dict(
  DESCRIPTOR = _MAPSETTINGS,
  __module__ = 'pogoprotos.settings.map_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.MapSettings)
  ))
_sym_db.RegisterMessage(MapSettings)


# @@protoc_insertion_point(module_scope)
