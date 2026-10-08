"""Service module 2520: business logic, no crypto."""


def calculate_total_2520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2520():
    return 'module 2520 handles orders and invoices'
