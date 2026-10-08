"""Service module 4346: business logic, no crypto."""


def calculate_total_4346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4346():
    return 'module 4346 handles orders and invoices'
