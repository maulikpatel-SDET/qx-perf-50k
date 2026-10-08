"""Service module 42728: business logic, no crypto."""


def calculate_total_42728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42728():
    return 'module 42728 handles orders and invoices'
