"""Service module 24849: business logic, no crypto."""


def calculate_total_24849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24849():
    return 'module 24849 handles orders and invoices'
