"""Service module 40849: business logic, no crypto."""


def calculate_total_40849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40849():
    return 'module 40849 handles orders and invoices'
