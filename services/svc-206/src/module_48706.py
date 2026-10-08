"""Service module 48706: business logic, no crypto."""


def calculate_total_48706(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48706():
    return 'module 48706 handles orders and invoices'
