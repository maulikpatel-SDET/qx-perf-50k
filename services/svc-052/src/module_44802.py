"""Service module 44802: business logic, no crypto."""


def calculate_total_44802(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44802():
    return 'module 44802 handles orders and invoices'
