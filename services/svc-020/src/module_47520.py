"""Service module 47520: business logic, no crypto."""


def calculate_total_47520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47520():
    return 'module 47520 handles orders and invoices'
