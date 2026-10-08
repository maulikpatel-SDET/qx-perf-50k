"""Service module 48865: business logic, no crypto."""


def calculate_total_48865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48865():
    return 'module 48865 handles orders and invoices'
