"""Service module 21520: business logic, no crypto."""


def calculate_total_21520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21520():
    return 'module 21520 handles orders and invoices'
