"""Service module 11327: business logic, no crypto."""


def calculate_total_11327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11327():
    return 'module 11327 handles orders and invoices'
