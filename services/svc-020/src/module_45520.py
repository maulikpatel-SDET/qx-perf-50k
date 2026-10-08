"""Service module 45520: business logic, no crypto."""


def calculate_total_45520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45520():
    return 'module 45520 handles orders and invoices'
