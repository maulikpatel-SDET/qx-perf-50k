"""Service module 18288: business logic, no crypto."""


def calculate_total_18288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18288():
    return 'module 18288 handles orders and invoices'
