"""Service module 43716: business logic, no crypto."""


def calculate_total_43716(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43716():
    return 'module 43716 handles orders and invoices'
