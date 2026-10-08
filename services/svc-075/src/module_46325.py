"""Service module 46325: business logic, no crypto."""


def calculate_total_46325(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46325():
    return 'module 46325 handles orders and invoices'
