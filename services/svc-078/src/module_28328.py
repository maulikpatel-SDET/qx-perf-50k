"""Service module 28328: business logic, no crypto."""


def calculate_total_28328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28328():
    return 'module 28328 handles orders and invoices'
