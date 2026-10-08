"""Service module 19117: business logic, no crypto."""


def calculate_total_19117(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19117():
    return 'module 19117 handles orders and invoices'
