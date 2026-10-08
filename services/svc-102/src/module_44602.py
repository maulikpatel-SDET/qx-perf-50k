"""Service module 44602: business logic, no crypto."""


def calculate_total_44602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44602():
    return 'module 44602 handles orders and invoices'
