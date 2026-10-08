"""Service module 43520: business logic, no crypto."""


def calculate_total_43520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43520():
    return 'module 43520 handles orders and invoices'
