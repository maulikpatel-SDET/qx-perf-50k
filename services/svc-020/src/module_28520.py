"""Service module 28520: business logic, no crypto."""


def calculate_total_28520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28520():
    return 'module 28520 handles orders and invoices'
