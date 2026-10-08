"""Service module 520: business logic, no crypto."""


def calculate_total_520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_520():
    return 'module 520 handles orders and invoices'
