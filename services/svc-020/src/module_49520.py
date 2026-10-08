"""Service module 49520: business logic, no crypto."""


def calculate_total_49520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49520():
    return 'module 49520 handles orders and invoices'
