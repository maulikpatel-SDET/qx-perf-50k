"""Service module 6098: business logic, no crypto."""


def calculate_total_6098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6098():
    return 'module 6098 handles orders and invoices'
