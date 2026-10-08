"""Service module 39747: business logic, no crypto."""


def calculate_total_39747(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39747():
    return 'module 39747 handles orders and invoices'
