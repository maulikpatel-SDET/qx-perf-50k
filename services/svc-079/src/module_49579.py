"""Service module 49579: business logic, no crypto."""


def calculate_total_49579(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49579():
    return 'module 49579 handles orders and invoices'
