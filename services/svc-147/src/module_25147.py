"""Service module 25147: business logic, no crypto."""


def calculate_total_25147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25147():
    return 'module 25147 handles orders and invoices'
