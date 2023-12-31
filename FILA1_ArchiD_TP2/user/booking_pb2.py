# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto

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
  name='booking.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rbooking.proto\"\x14\n\x06UserID\x12\n\n\x02id\x18\x01 \x01(\t\"3\n\x0b\x42ookingData\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x14\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\x05.Date\"$\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\";\n\nNewBooking\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0f\n\x07movieid\x18\x03 \x01(\t\"\x0e\n\x0c\x45mptyBooking2\x9b\x01\n\x07\x42ooking\x12\x31\n\x0eGetAllBookings\x12\r.EmptyBooking\x1a\x0c.BookingData\"\x00\x30\x01\x12+\n\x10GetBookingByUser\x12\x07.UserID\x1a\x0c.BookingData\"\x00\x12\x30\n\x11PostBookingByUser\x12\x0b.NewBooking\x1a\x0c.BookingData\"\x00\x62\x06proto3')
)




_USERID = _descriptor.Descriptor(
  name='UserID',
  full_name='UserID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UserID.id', index=0,
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
  serialized_start=17,
  serialized_end=37,
)


_BOOKINGDATA = _descriptor.Descriptor(
  name='BookingData',
  full_name='BookingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='BookingData.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dates', full_name='BookingData.dates', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=39,
  serialized_end=90,
)


_DATE = _descriptor.Descriptor(
  name='Date',
  full_name='Date',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='Date.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='movies', full_name='Date.movies', index=1,
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
  serialized_start=92,
  serialized_end=128,
)


_NEWBOOKING = _descriptor.Descriptor(
  name='NewBooking',
  full_name='NewBooking',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='NewBooking.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='NewBooking.date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='movieid', full_name='NewBooking.movieid', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=130,
  serialized_end=189,
)


_EMPTYBOOKING = _descriptor.Descriptor(
  name='EmptyBooking',
  full_name='EmptyBooking',
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
  serialized_start=191,
  serialized_end=205,
)

_BOOKINGDATA.fields_by_name['dates'].message_type = _DATE
DESCRIPTOR.message_types_by_name['UserID'] = _USERID
DESCRIPTOR.message_types_by_name['BookingData'] = _BOOKINGDATA
DESCRIPTOR.message_types_by_name['Date'] = _DATE
DESCRIPTOR.message_types_by_name['NewBooking'] = _NEWBOOKING
DESCRIPTOR.message_types_by_name['EmptyBooking'] = _EMPTYBOOKING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserID = _reflection.GeneratedProtocolMessageType('UserID', (_message.Message,), dict(
  DESCRIPTOR = _USERID,
  __module__ = 'booking_pb2'
  # @@protoc_insertion_point(class_scope:UserID)
  ))
_sym_db.RegisterMessage(UserID)

BookingData = _reflection.GeneratedProtocolMessageType('BookingData', (_message.Message,), dict(
  DESCRIPTOR = _BOOKINGDATA,
  __module__ = 'booking_pb2'
  # @@protoc_insertion_point(class_scope:BookingData)
  ))
_sym_db.RegisterMessage(BookingData)

Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), dict(
  DESCRIPTOR = _DATE,
  __module__ = 'booking_pb2'
  # @@protoc_insertion_point(class_scope:Date)
  ))
_sym_db.RegisterMessage(Date)

NewBooking = _reflection.GeneratedProtocolMessageType('NewBooking', (_message.Message,), dict(
  DESCRIPTOR = _NEWBOOKING,
  __module__ = 'booking_pb2'
  # @@protoc_insertion_point(class_scope:NewBooking)
  ))
_sym_db.RegisterMessage(NewBooking)

EmptyBooking = _reflection.GeneratedProtocolMessageType('EmptyBooking', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYBOOKING,
  __module__ = 'booking_pb2'
  # @@protoc_insertion_point(class_scope:EmptyBooking)
  ))
_sym_db.RegisterMessage(EmptyBooking)



_BOOKING = _descriptor.ServiceDescriptor(
  name='Booking',
  full_name='Booking',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=208,
  serialized_end=363,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllBookings',
    full_name='Booking.GetAllBookings',
    index=0,
    containing_service=None,
    input_type=_EMPTYBOOKING,
    output_type=_BOOKINGDATA,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBookingByUser',
    full_name='Booking.GetBookingByUser',
    index=1,
    containing_service=None,
    input_type=_USERID,
    output_type=_BOOKINGDATA,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PostBookingByUser',
    full_name='Booking.PostBookingByUser',
    index=2,
    containing_service=None,
    input_type=_NEWBOOKING,
    output_type=_BOOKINGDATA,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKING)

DESCRIPTOR.services_by_name['Booking'] = _BOOKING

# @@protoc_insertion_point(module_scope)
