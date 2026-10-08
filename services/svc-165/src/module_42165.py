"""Service module 42165: business logic, no crypto."""


def calculate_total_42165(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42165():
    return 'module 42165 handles orders and invoices'
