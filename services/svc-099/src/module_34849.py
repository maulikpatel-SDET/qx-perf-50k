"""Service module 34849: business logic, no crypto."""


def calculate_total_34849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34849():
    return 'module 34849 handles orders and invoices'
