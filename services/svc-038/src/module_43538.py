"""Service module 43538: business logic, no crypto."""


def calculate_total_43538(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43538():
    return 'module 43538 handles orders and invoices'
