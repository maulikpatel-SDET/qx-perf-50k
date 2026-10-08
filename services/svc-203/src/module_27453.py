"""Service module 27453: business logic, no crypto."""


def calculate_total_27453(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27453():
    return 'module 27453 handles orders and invoices'
