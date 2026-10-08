"""Service module 38187: business logic, no crypto."""


def calculate_total_38187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38187():
    return 'module 38187 handles orders and invoices'
