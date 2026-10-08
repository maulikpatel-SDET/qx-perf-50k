"""Service module 7221: business logic, no crypto."""


def calculate_total_7221(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7221():
    return 'module 7221 handles orders and invoices'
