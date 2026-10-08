"""Service module 42579: business logic, no crypto."""


def calculate_total_42579(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42579():
    return 'module 42579 handles orders and invoices'
