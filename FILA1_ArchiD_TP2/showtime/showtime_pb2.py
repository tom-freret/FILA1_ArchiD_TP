# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: showtime.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='showtime.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0eshowtime.proto\"\x1c\n\x0cScheduleDate\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"(\n\x08Schedule\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"(\n\tSchedules\x12\x1b\n\x08schedule\x18\x01 \x03(\x0b\x32\t.Schedule\"\x0f\n\rEmptySchedule2n\n\x08Showtime\x12/\n\x11GetScheduleByDate\x12\r.ScheduleDate\x1a\t.Schedule\"\x00\x12\x31\n\x0fGetAllSchedules\x12\x0e.EmptySchedule\x1a\n.Schedules\"\x00\x30\x01\x62\x06proto3')
)




_SCHEDULEDATE = _descriptor.Descriptor(
  name='ScheduleDate',
  full_name='ScheduleDate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='ScheduleDate.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=46,
)


_SCHEDULE = _descriptor.Descriptor(
  name='Schedule',
  full_name='Schedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='Schedule.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='movies', full_name='Schedule.movies', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=88,
)


_SCHEDULES = _descriptor.Descriptor(
  name='Schedules',
  full_name='Schedules',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedule', full_name='Schedules.schedule', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=130,
)


_EMPTYSCHEDULE = _descriptor.Descriptor(
  name='EmptySchedule',
  full_name='EmptySchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=147,
)

_SCHEDULES.fields_by_name['schedule'].message_type = _SCHEDULE
DESCRIPTOR.message_types_by_name['ScheduleDate'] = _SCHEDULEDATE
DESCRIPTOR.message_types_by_name['Schedule'] = _SCHEDULE
DESCRIPTOR.message_types_by_name['Schedules'] = _SCHEDULES
DESCRIPTOR.message_types_by_name['EmptySchedule'] = _EMPTYSCHEDULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScheduleDate = _reflection.GeneratedProtocolMessageType('ScheduleDate', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULEDATE,
  __module__ = 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:ScheduleDate)
  ))
_sym_db.RegisterMessage(ScheduleDate)

Schedule = _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULE,
  __module__ = 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:Schedule)
  ))
_sym_db.RegisterMessage(Schedule)

Schedules = _reflection.GeneratedProtocolMessageType('Schedules', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULES,
  __module__ = 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:Schedules)
  ))
_sym_db.RegisterMessage(Schedules)

EmptySchedule = _reflection.GeneratedProtocolMessageType('EmptySchedule', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYSCHEDULE,
  __module__ = 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:EmptySchedule)
  ))
_sym_db.RegisterMessage(EmptySchedule)



_SHOWTIME = _descriptor.ServiceDescriptor(
  name='Showtime',
  full_name='Showtime',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=149,
  serialized_end=259,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetScheduleByDate',
    full_name='Showtime.GetScheduleByDate',
    index=0,
    containing_service=None,
    input_type=_SCHEDULEDATE,
    output_type=_SCHEDULE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllSchedules',
    full_name='Showtime.GetAllSchedules',
    index=1,
    containing_service=None,
    input_type=_EMPTYSCHEDULE,
    output_type=_SCHEDULES,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SHOWTIME)

DESCRIPTOR.services_by_name['Showtime'] = _SHOWTIME

# @@protoc_insertion_point(module_scope)
